:: Check if a Python Virtual Envrionment exists
if exist .venv (
    :: Activate the Python Virtual Envrionment
    Call .\.venv\Scripts\activate
) else (
    :: Create a Python virtual Envrionment
    python -m venv .venv

    :: Activate the Python Virtual Envrionment
    Call .\.venv\Scripts\activate

    :: Install Python side packages
    pip install -r .\requirements.txt
)

:: Execute the program
cd .\src\
py .\__main__.py
