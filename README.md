# Weather App CLI

A simple, modular Python command-line application to fetch and display the current weather and 1-day forecast for any city using the [WeatherAPI.com](https://www.weatherapi.com/) service.

---

## 📝 Table of Contents

* [Features](#features)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Configuration](#configuration)
* [Usage](#usage)
* [Testing](#testing)
* [Project Structure](#project-structure)
* [Contributing](#contributing)
* [License](#license)

---

## 🚀 Features

* Fetch current weather and forecast (1-day) for any city
* Display place name, temperature (actual & feels like), condition, wind, humidity, and UV index
* Show sunrise, sunset, min/max/avg temperatures, wind, precipitation, and chance of rain
* Clean, modular codebase with:

  * `weather/api.py` for API requests
  * `weather/display.py` for formatting output
  * `weather/config.py` for environment variable management
* Flexible CLI using Python’s `argparse`
* Unit tests with `pytest` for both API layer and display formatting

---

## ⚙️ Prerequisites

* Python 3.7 or higher
* A free API key from [WeatherAPI.com](https://www.weatherapi.com/) (sign up for a free account to obtain your key)
* `pip` (Python package manager)

---

## 📦 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/tu-usuario/weather_app.git
   cd weather_app
   ```

2. **Create a virtual environment** (recommended)

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate    # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🔧 Configuration

1. **Create a `.env` file** in the project root:

   ```env
   API_KEY=your_weatherapi_key_here
   ```

2. Ensure the variable name matches exactly (`API_KEY`).

---

## 💻 Usage

Run the CLI script with the target city as an argument:

```bash
python cli.py "Lima"
```

Example output:

```text
* WEATHER IN LIMA, LIMA - Peru (last updated: 2025-05-26 09:00)
Temperature: 22 °C -> Feels like: 23 °C
Condition: Partly cloudy
Wind: 15 km/h
Humidity: 60%
UV: 4

---------------------------------------------------------------------

* FORECAST -> 2025-05-27
Sunrise: 06:15 AM | Sunset: 05:45 PM
Temp. Min: 18°C | Max: 28°C | AVG: 23°C
Max Wind: 20 km/h | Precipitation: 0.0 mm
AVG Humidity: 55% | Chance of rain: 10%
```

You can integrate additional flags in the future (e.g., `--days`, `--units`).

---

## 🧪 Testing

Ensure you have `pytest` installed (it's included in `requirements.txt`):

```bash
pytest --maxfail=1 --disable-warnings -q
```

You should see all tests passing:

```bash
...  [100%]
```

---

## 📁 Project Structure

```
weather_app/
├── weather/           # Package modules
│   ├── __init__.py    # Package initializer
│   ├── api.py         # API request & parsing logic
│   ├── display.py     # Formatting & output functions
│   └── config.py      # Environment variable loader
├── tests/             # Test suite
│   ├── test_api.py    # Tests for API layer
│   └── test_display.py# Tests for display formatting
├── cli.py             # Command-line interface entry point
├── requirements.txt   # Python dependencies
├── .env.example       # Example environment file (rename to .env)
├── .gitignore         # Files and folders to ignore in git
└── README.md          # This file
```

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a pull request

Please ensure tests pass and follow the existing code style.

---

## 📄 License

You can choose an open-source license that best suits your project and sharing preferences. Common options include:

* **MIT License:** Permissive and widely used, allows reuse with minimal restrictions.
* **Apache 2.0 License:** Permissive, includes explicit patent grant.
* **GPLv3 License:** Copyleft, requires derivative works to use the same license.

To apply a license:

1. Create a `LICENSE` file in the project root containing the full text of the chosen license.
2. Update this section with a short description and link to the `LICENSE` file.

If you prefer not to include a license, you can remove this section entirely. Feel free to adjust according to your needs.