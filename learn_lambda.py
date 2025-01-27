def learn_lambda(event, context):

    first_name = event['first_name']
    last_name = event['last_name']

    message = f"Hello {first_name} {last_name}!"

    return message