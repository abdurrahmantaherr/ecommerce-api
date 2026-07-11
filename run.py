from app import create_app
print("Starting/........")
app = create_app()

if __name__ == "__main__":
    print("Runnig....")
    app.run(debug=True)