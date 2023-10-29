import streamlit as st
import requests

st.markdown(
    """
    <style>
    body {
        background-color: red;
        color: white;
    }
    .p{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    .center {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    .button{
        display: flex;
        justify-content: center;
        align-items: center;    
    }
    </style>
    """,
    unsafe_allow_html=True
)



def Get_Response(location):
    url = "http://api.weatherstack.com/current"

    params = {
        'access_key': '1d8cccd09c5125b00a89e4bcf4e0e91a',
        'query': location
    }

    response = requests.get(url, params)

    if response.status_code == 200:
        data = response.json()
        current_data = data.get("current", {})
        temperature = current_data.get("temperature", "N/A")
        wind_speed = current_data.get("wind_speed", "N/A")
        humidity = current_data.get("humidity", "N/A")
        return temperature, wind_speed, humidity
    else:
        return None, None, None


def Get_Forecast(location):
    params = {
        'access_key': '1d8cccd09c5125b00a89e4bcf4e0e91a',
        'query': location,
        'forecast_days' : '1'
    }

    api_result = requests.get('https://api.weatherstack.com/forcast', params)

    response = api_result.json()

    if response.status_code == 200:
        api_response = response.json()
        return u'The temperature in %s tomorrow is %d℃' % (api_response['location']['name'], api_response['forcast']['temperature'])
    else:
        return 'Failed to retrieve data, please try again'


st.markdown('<h1 style="text-align: center; font: bold; color:#41ccb3;">Weather Forecast</h1>', unsafe_allow_html=True)

st.image("weather-icon-sun-and-cloud-icon-png.webp", caption="", use_column_width=True)

col_left, col_middle, col_right, col_extra = st.columns(4)

location = st.text_input("Enter a location", key="location")

button_key = "get_weather_button"
forecast_button_key = "get_forecast_button"

if st.button("Get Current Weather", key=button_key):
    temperature, wind_speed, humidity = Get_Response(location)
    col_left.metric('Temperature', f"{temperature} ℃" if temperature is not None else "N/A", 'normal')
    col_middle.metric('Wind Speed', f"{wind_speed} mph" if wind_speed is not None else "N/A", 'normal')
    col_right.metric('Humidity', f"{humidity} %" if humidity is not None else "N/A", 'normal')































