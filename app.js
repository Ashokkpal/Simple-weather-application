function getWeather() {
    const city = document.getElementById("city").value;
    if (!city) {
        alert("Please enter a city name.");
        return;
    }

    fetch(`/get_weather?city=${city}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                document.getElementById("city-name").textContent = data.city;
                document.getElementById("temp").textContent = `Temperature: ${data.temperature} °C`;
                document.getElementById("description").textContent = `Condition: ${data.description}`;
                document.getElementById("icon").src = `http://openweathermap.org/img/wn/${data.icon}.png`;
            }
        })
        .catch(error => {
            console.error("Error fetching weather data:", error);
            alert("Error fetching weather data. Please try again.");
        });
}
