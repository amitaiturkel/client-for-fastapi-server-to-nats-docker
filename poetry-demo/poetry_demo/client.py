import httpx


async def interact_with_calculator_server():
    id = input("what it your id?")
    port = input("what is the port of the nats you want to connect?")
    print("Welcome to the calculator program. Enter 'Q' to quit at any time.")

    while True:
        operator = input("Enter an operator ('add', 'subtract', 'multiply', 'divide', 'clear', 'put_in') or 'Q' to quit: ")

        if operator.lower() == "q":
            print("Exiting the program.")
            break

        if operator not in ["add", "subtract", "multiply", "divide", "clear", "put_in"]:
            print("Invalid operator. Please enter a valid operator or 'Q' to quit.")
            continue
        if operator != "clear":
            try:
                num = float(input("Enter a number: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue
        else:
            num = 0


        url = "http://localhost:8000/connect-nats"  # URL of the calculator service

        headers = {"user-id": f"{id}" , "operator" : f"{operator}", "num" : f"{num}","port" : f"{port}"}  # desired user agent

        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers,timeout=20)

        if response.status_code == 200:
            result = response.json()["result"]
            print(f"Result: {result}")
        else:
            print("An error occurred while communicating with the calculator service.error code is ", response.status_code, url)


if __name__ == "__main__":
    import asyncio
    asyncio.run(interact_with_calculator_server())