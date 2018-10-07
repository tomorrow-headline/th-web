# Tomorrow Headline

## Intro

Deploy source code in this repo for developing reason.

## Steps

### Prerequisites

- [Python 3](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installing/)
- [nodejs](https://nodejs.org/en/download/package-manager/)

You need to place source code from [th-web-frontend](https://github.com/tomorrow-headline/th-web-frontend) and [th-web-backend](https://github.com/tomorrow-headline/th-web-backend) as follow:

```
└── tomorrow-headline
    ├── th-web-backend
    │   ├── doc
    │   ├── README.md
    │   ├── requirements.txt
    │   └── src
    └── th-web-frontend
        ├── build
        ├── config
        ├── dist
        ├── index.html
        ├── node_modules
        ├── package.json
        ├── package-lock.json
        ├── README.md
        ├── src
        └── static
```

### Install Dependency Package

```
pip install -r requirements.txt
npm install
```

### Collect Statics in Django

```
cd th-web-backend/src
./manage.py collectstatic # Using Python3, virtual environment recommended.
```

### Build `th-web-frontend`

```
cd th-web-frontend
npm install
npm run build
```

### Finish

```
cd th-web-backend/src
./manage.py runserver
```

Then open http://127.0.0.1:8000/.
