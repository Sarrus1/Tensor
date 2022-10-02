# Tensor community's Website

This repository hosts the internal files of the [Tensor community's website](https://tensor.fr), under the MIT license. Although I won't offer bug support, educated questions regarding the code are welcome.

## Intents

This website intents to provide stats for players, a management interface for the owner and the admins. This includes automated servers control through the [LGSM Project](https://linuxgsm.com/), [SourceBans++](https://sbpp.dev/) integration, [RankMe](https://github.com/Sarrus1/kento-rankme) integration, [SurfTimer](https://github.com/surftimer/Surftimer-Official) integration, as well as [tVip](https://github.com/Sarrus1/tvip) integration with an automated donation system using the Paypal SDK.

Other features include, while not limited to, server statistics collection using the [A2S protocol](https://developer.valvesoftware.com/wiki/Server_queries), various integrations with the Steam API, automatic scoreboard notification with a Discord server, automated admin application process with Discord integration, and an API for the community's Discord BOT.

This project is by no means meant for external use, outside of the Tensor community, meaning the maintainers won't provide support for it. However, feel free to adapt the code to your needs, following the [MIT License](https://en.wikipedia.org/wiki/MIT_License) guidelines.

## CD/CI

Tests haven't yet been implemented in the project, however Continuous Integration is used to deploy the update whenever something is pushed to the main branch. For more details on the deploy script running on our server, feel free to contact me.

## Requirements (for collaborators)

- Python3 (Tested with 3.10)
- Node.js (16.13.2) and npm (latest)

## Installation (for collaborators)

1. Backend

- Clone this repository.
- Go to `backend/`.
- Create the `backend/.env` file following the `backend/.env.sample.txt` template.
- Create a virtual environment with `python3 -m virtualenv env` or `python -m virtualenv env` or (for Windows) `py -m virtualenv env`.
- Activate your virtual environment with `source env/bin/activate` or (for Windows) `env\Scripts\activate.bat`.
- Install the required modules with `pip install -r requirements.txt`.
- Make your migrations with `python manage.py migrate` or (for Windows) `py manage.py migrate` (if this fails, go down to the N.B section).

1. Frontend

- Go to `frontend/src`.
- Install the node modules using `npm i`.
- Transpile the React code using `npm run watch`.

## N.B

- The following fixes may not apply anymore.
- During the installation for development, there might be an issue while creating the database. To solve it, you have to comment out the `StandardResultsSetPagination` class of `backend/servers/views.py` and comment out the `pagination_class` line of the same file, while you apply the migrations.
- The issue comes from the lack of migrations for database tables managed by SourceMod plugins. In the future, I will add some fixtures to fix this.
