import yfinance as yf

def extract_data(ticker):
    data = yf.Ticker(ticker)
    history = data.history(period="1y")
    return history

if __name__ == "__main__":
    df = extract_data("JPM")  # Prueba con JP Morgan
    print(df.head())  # Ver primeras filas
 