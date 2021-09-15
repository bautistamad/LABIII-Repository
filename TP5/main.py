import requests

def main():
    print("Comienza la API")
    api_link = "https://api.covid19api.com/live/country/argentina"
    response = requests.get(api_link)
    print(response.status_code)


if __name__ == "__main__":
    main()