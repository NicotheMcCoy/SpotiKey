# SpotiKey

## Overview

**SpotiKey** uncovers the musical DNA of your favorite Spotify tracks...

![App Screenshot](/test.png)

## Features

- **Key Discovery**: Identify the musical key of any track with ease.
- **Modality Information**: Find out whether your song is in a major or minor key.
- **BPM Analysis**: Discover the Tempo/BPM of your selected track. 

## Getting Started

### Prerequisites

- Python 3.x
- A [Spotify Developer account](https://developer.spotify.com/dashboard/) and API credentials

### Installation and Setup

1. **Clone the Repository**
    ```sh
    git clone https://github.com/nicothemccoy/SpotiKey.git
    ```
2. **Install Dependencies**
    ```sh
    pip install -r requirements.txt
    ```

3. **Setup API Credentials**

   - Navigate to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
   - Copy the Client ID and Client Secret.
   - Rename .env.example to .env and replace the placeholders with your API credentials.

4. **Run SpotiKey**
    ```
    python spotikey.py
    ```
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.
