# kinova-control

A devcontainer environment for developing control software for Kinova robots.

In order to build the Docker container for the environment,

- Create `libraries` folder under `kinova-control/.devcontainer/robot`
- Download [Kortex API](https://artifactory.kinovaapps.com/ui/api/v1/download?repoKey=generic-public&path=kortex%2FAPI%2F2.5.0%2Fkortex_api-2.5.0.post6-py3-none-any.whl) to `libraries` folder
- In Visual Studio Code:
	- Open the `kinova-control` folder in VS Code
	- Open command palette with `Ctrl+Shift+P`
	- Type: `Dev Containers: Reopen in Container`
