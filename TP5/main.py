import requests
import plotly.graph_objects as go

def main():
    print("Comienza la API")
    api_link = "https://api.covid19api.com/total/dayone/country/argentina/status/confirmed"
    response = requests.get(api_link)
    print(response.status_code)
    respuesta = response.json()
    #print(respuesta)
    mes = "06"
    anio = "2020"
    casos  = []

    for singular in respuesta:
        if singular["Date"].split('-')[0] == anio and singular["Date"].split('-')[1] == mes:
            print(singular['Date'])
            casos.append(singular['Cases'])
    #for case in respuesta:
    #    print(["Confirmed"])

    fig = go.Figure(
    data=[go.Bar(y=casos)],
    layout_title_text="A Figure Displayed with fig.show()"
    )
    fig.show()

if __name__ == "__main__":
    main()