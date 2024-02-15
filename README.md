# msganalyser

A dashboard for Messenger (Meta) data analysis.

# How to use it

### 1. Download this repo (or clone it).

### 2. Make sure you've got Node.js and Python (>=3.10) installed.

### 3. Use the ready-made scripts to run the app:

**Windows users:**

Run two scripts located in the `scripts-windows` folder. In case they fail to fully execute, open two terminals in this folder (one for each script) and manually copy scripts contents to terminals and run them line-by-line. 

**Linux users:**

Open the terminal at the root location of the project and run the scripts located in the `scripts` folder in two separate terminals:
```bash
./scripts/backend-setup.sh
```
```bash
./scripts/frontend-setup.sh
```

### 4. Visit `http://localhost:3000/` in your browser

### 5. Place all your Facebook zipped data in the `data` folder.

Only messages data is needed.

### 6. On the setup page:

- Leave the "Path to the folder with Facebook data" field with the default value (unless you placed your data elsewhere than specified in the previous step);
- Customise other options to your liking;
- Press "Load your data" and wait. This could take a few minutes, depending on the size of the data.

### 7. Once the data is loaded, a link to the dashboard will pop up below the setup form.

There you will further instructions and various analysis of your data. Enjoy browsing!

# Technical details

Frameworks used:

**Backend:**
- Python,
- FastAPI,
- pandas.

**Frontend:**
- TypeScript,
- Vue 3,
- Nuxt,
- Chart.js,
- Tailwindcss.

# Screenshots

### Setup page:

![setup page](https://firebasestorage.googleapis.com/v0/b/my-projects-showcase.appspot.com/o/app-screenshots%2F6%2Fmsganalyser1.png?alt=media&token=7a70c81a-3ebc-49a2-b76d-a6668adefa0a)

### Dashboard home:

![dashboard home](https://firebasestorage.googleapis.com/v0/b/my-projects-showcase.appspot.com/o/app-screenshots%2F6%2Fmsganalyser2.png?alt=media&token=3567cd06-753c-4cd9-bbf1-05f5cf273e3a)

### Filters:

![filters](https://firebasestorage.googleapis.com/v0/b/my-projects-showcase.appspot.com/o/app-screenshots%2F6%2Fmsganalyser3.png?alt=media&token=ded4215d-1a71-413c-9ee3-197c25d12884)

### Example plot:

![example plot](https://firebasestorage.googleapis.com/v0/b/my-projects-showcase.appspot.com/o/app-screenshots%2F6%2Fmsganalyser4.png?alt=media&token=4c201707-4aca-448d-ae50-83982785830c)

### Example table:

![example table](https://firebasestorage.googleapis.com/v0/b/my-projects-showcase.appspot.com/o/app-screenshots%2F6%2Fmsganalyser5.png?alt=media&token=b496d049-8327-4df5-a0fa-51e8efbc21d0)
