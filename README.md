M23 Language

M23 is a human-friendly, English-like programming language designed for Data Science, Machine Learning, CSV/Table manipulation, Database, API, and multi-language workflows.

It is built on Python but allows seamless integration with:

SQL (PostgreSQL, MySQL, SQLite)

Rust (high-performance computation via PyO3)

C++ (via pybind11 for performance-heavy tasks)

R (statistics & visualization via rpy2)

JavaScript/TypeScript (export JSON for frontend charts)

HTML/CSS (report generation)

Features

Load, filter, and manipulate CSV and table data

Generate charts (line, bar) using built-in runtime functions

Train Machine Learning models with scikit-learn

Fetch and process API data

SQL database integration

Multi-language support: Python + Rust + C++ + R + JS + HTML

Case-insensitive and typo-tolerant syntax

English-like, easy-to-read code

Installation

Clone the repository:

git clone https://github.com/yourusername/m23.git
cd m23


Install dependencies:

pip install -r requirements.txt

Usage

Run any .m23 script using the interpreter:

python m23.py examples/csv_example.m23


Or using the package entry point:

python -m m23 examples/multi_lang_workflow.m23

Examples
CSV & Table Operations
LOAD CSV "sales.csv" AS sales
sales -> select columns ["date" "region" "revenue"]
sales -> filter revenue > 1000
show sales -> head 5
save sales as "filtered_sales.csv"

Machine Learning
from sklearn.linear_model import LinearRegression
train model HouseModel = LinearRegression on X y

Multi-Language Workflow

Python + Rust + C++ + SQL + R + JS + HTML

Example: examples/multi_lang_workflow.m23

Folder Structure
M23/
 ├─ m23.py
 ├─ runtime.py
 ├─ examples/
 ├─ docs/
 ├─ requirements.txt
 ├─ README.md
 └─ LICENSE

License

M23 is released under the MIT License. See the LICENSE file for details.

