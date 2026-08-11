# SMART-NAVI Frontend

This is the frontend for the SMART-NAVI application, built with [React](https://react.dev/) and [Vite](https://vitejs.dev/).

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need [Node.js](https://nodejs.org/) installed on your machine. This project requires **Node.js version 18 or higher**.

We strongly recommend using a node version manager like [nvm](https://github.com/nvm-sh/nvm) to manage your Node.js versions.

To install the latest Long-Term Support (LTS) version of Node.js with `nvm`, run:
```bash
nvm install --lts
nvm use --lts
```

### Installation

1.  **Clone the repository** (if you haven't already):
    ```bash
    git clone <your-repository-url>
    ```

2.  **Navigate to the project directory**:
    ```bash
    cd SMART-NAVI/frontend
    ```

3.  **Install dependencies**:
    This command reads the `package.json` file and downloads all the required libraries (like React and Vite) into a `node_modules` folder.
    ```bash
    npm install
    ```

## Available Scripts

In the project directory, you can run the following commands:

### `npm run dev`
Runs the app in development mode. Open the URL provided in the terminal (usually `http://localhost:5173`) to view it in your browser. The page will automatically reload when you make code changes.

### `npm run build`
Builds the app for production into the `dist` folder. It bundles your code, optimizes it for performance, and gets it ready to be deployed to a web server.

### `npm run lint`
Runs the ESLint tool to analyze your code for potential errors and style issues. This helps maintain code quality and consistency.

### `npm run preview`
This command starts a local web server to preview your production build from the `dist` folder. It's a great way to check your final application before deploying it.
