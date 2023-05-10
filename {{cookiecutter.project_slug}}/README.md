# {{ cookiecutter.project_name }}

This project was bootstrapped with [cookiecutter-p8g](https://github.com/bernhardfritz/cookiecutter-p8g).

## Available Scripts

In the project directory, you can run:

### `{{ cookiecutter.package_manager }}{% if cookiecutter.package_manager != "yarn" %} run{% endif %} dev`

Runs the app in the development mode.\
Open [http://localhost:5173](http://localhost:5173) to view it in your browser.

The page will reload when you make changes.

### `{{ cookiecutter.package_manager }}{% if cookiecutter.package_manager != "yarn" %} run{% endif %} build`

Builds the app for production to the `dist` folder.

### `{{ cookiecutter.package_manager }}{% if cookiecutter.package_manager != "yarn" %} run{% endif %} preview`

Previews the production build locally.

## Learn More

You can learn more in the [p8g documentation](https://bernhardfritz.github.io/p8g).
