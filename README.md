# ConvPy

This Python script, `ConvPy`, is a tool that fetches data about currency exchange rates from the Central Bank of Russia (CBR) API and provides information about specific currencies based on user input. It utilizes the `requests` library to retrieve JSON data from the CBR API and then parses and presents the currency data.

## Usage

1. **Installation**: Ensure you have Python installed on your system. If not, you can download and install it from [Python's official website](https://www.python.org/).

2. **Clone the Repository**: Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/citizen322/ConvPy
   ```
   
3. **Navigate to the Directory**: Move to the directory containing the cloned repository:

   ```bash
   cd ConvPy
   ```

4. **Run the Script**: Execute the Python script `currency_converter.py` using the following command:

   ```bash
   python main.py
   ```

5. **Input**: When prompted, enter the currency code (e.g., USD, EUR) or the name of the currency you want to retrieve information about.

6. **Output**: The script will display the current and previous exchange rates for the specified currency.

## Requirements

- Python 3.x
- requests library (install using `pip install requests` if not already installed)
