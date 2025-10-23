import sys
import pandas as pd
from sklearn.linear_model import LinearRegression
import difflib
# Instead of `import runtime`

# Import runtime.py from the same folder
import m23.runtime as runtime  # <-- updated import

# -----------------------------
# Keyword list for typo tolerance
# -----------------------------
KEYWORDS = [
    "load", "csv", "as", "select", "columns", "filter",
    "where", "show", "head", "train", "model", "on",
    "with", "params", "save", "plot", "fetch", "run",
    "type", "x", "y", "title"
]

def suggest_keyword(word):
    matches = difflib.get_close_matches(word.lower(), KEYWORDS, n=1, cutoff=0.6)
    return matches[0] if matches else word

# -----------------------------
# Parse and execute a single line
# -----------------------------
def parse_line(line, variables):
    line = line.strip()
    if not line or line.startswith("#"):  # skip empty/comment lines
        return

    # Normalize spaces
    line = ' '.join(line.split())
    tokens = line.split(" ")

    # Case-insensitive
    tokens = [t.lower() for t in tokens]

    # -----------------------------
    # LOAD CSV
    # -----------------------------
    if "load" in tokens and "csv" in tokens:
        idx = tokens.index("csv")
        path = tokens[idx + 1].strip('"').strip("'")
        name = "data"
        if "as" in tokens:
            name = tokens[tokens.index("as") + 1]
        df = pd.read_csv(path)
        variables[name] = df
        print(f"[INFO] Loaded CSV '{path}' as '{name}'")

    # -----------------------------
    # SELECT COLUMNS
    # -----------------------------
    elif "select" in tokens and "columns" in tokens:
        name = list(variables.keys())[-1]  # last variable
        idx = tokens.index("columns")
        cols = [c.strip('",') for c in tokens[idx + 1:]]
        if name in variables:
            variables[name] = variables[name][cols]
            print(f"[INFO] Selected columns {cols} in '{name}'")

    # -----------------------------
    # FILTER
    # -----------------------------
    elif "filter" in tokens:
        name = list(variables.keys())[-1]
        idx = tokens.index("filter")
        cond_tokens = tokens[idx + 1:]
        if len(cond_tokens) >= 3:
            col, op, val = cond_tokens[:3]
            df = variables[name]
            try:
                val = float(val)
            except:
                pass
            if op == ">":
                variables[name] = df[df[col] > val]
            elif op == "<":
                variables[name] = df[df[col] < val]
            elif op == "==":
                variables[name] = df[df[col] == val]
            print(f"[INFO] Filter applied on '{name}'")

    # -----------------------------
    # SHOW / HEAD
    # -----------------------------
    elif "show" in tokens:
        name = list(variables.keys())[-1]
        df = variables[name]
        if "head" in tokens:
            idx = tokens.index("head")
            n = int(tokens[idx + 1]) if len(tokens) > idx + 1 else 5
            print(df.head(n))
        else:
            print(df)

    # -----------------------------
    # TRAIN MODEL (LinearRegression)
    # -----------------------------
    elif "train" in tokens and "model" in tokens:
        idx = tokens.index("model")
        model_name = tokens[idx + 1]
        idx_on = tokens.index("on")
        features = tokens[idx_on + 1].split(",")
        target = tokens[idx_on + 2] if len(tokens) > idx_on + 2 else features[-1]

        df_features = variables[features[0]] if len(features) == 1 else pd.concat([variables[f] for f in features], axis=1)
        df_target = variables[target]

        model = LinearRegression()
        model.fit(df_features.values.reshape(-1,1), df_target.values)
        variables[model_name] = model
        print(f"[INFO] Trained LinearRegression model '{model_name}'")

    # -----------------------------
    # PLOT (line / bar)
    # -----------------------------
    elif "plot" in tokens:
        name = list(variables.keys())[-1]
        df = variables[name]
        try:
            chart_type = tokens[tokens.index("type") + 1]
            x_col = tokens[tokens.index("x") + 1]
            y_col = tokens[tokens.index("y") + 1]
            title = None
            if "title" in tokens:
                title = ' '.join(tokens[tokens.index("title") + 1:])
            runtime.plot(df, x_col, y_col, chart_type, title)
        except Exception as e:
            print(f"[ERROR] Plot failed: {e}")

    # -----------------------------
    # FETCH (API / Website)
    # -----------------------------
    elif "fetch" in tokens:
        idx = tokens.index("fetch")
        url = tokens[idx + 1].strip('"').strip("'")
        data = runtime.fetch_json(url)
        name = "data_api"
        variables[name] = pd.DataFrame(data)
        print(f"[INFO] Fetched API data into '{name}'")

    # -----------------------------
    # SAVE (CSV / Model)
    # -----------------------------
    elif "save" in tokens:
        name = list(variables.keys())[-1]
        idx = tokens.index("as")
        path = tokens[idx + 1].strip('"').strip("'")
        runtime.save_csv(variables[name], path)

# -----------------------------
# Main function to run .m23 files
# -----------------------------
def main():
    if len(sys.argv) < 2:
        print("Usage: python interpreter.py <file.m23>")
        return

    file_path = sys.argv[1]
    variables = {}  # store dataframes, models, etc.

    try:
        with open(file_path, "r") as f:
            for line in f:
                parse_line(line, variables)
    except FileNotFoundError:
        print(f"[ERROR] File '{file_path}' not found.")
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    main()
def main(file_path=None):
    import sys
    if file_path is None:
        if len(sys.argv) < 2:
            print("Usage: python interpreter.py <file.m23>")
            return
        file_path = sys.argv[1]

    variables = {}  # store dataframes, models, etc.

    try:
        with open(file_path, "r") as f:
            for line in f:
                parse_line(line, variables)
    except FileNotFoundError:
        print(f"[ERROR] File '{file_path}' not found.")
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    main()
