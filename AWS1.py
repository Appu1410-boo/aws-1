import json

def lambda_handler(event, context):
    try:
        number1 = event.get('number1')
        number2 = event.get('number2')
        
        if number1 is None or number2 is None:
            raise ValueError("Both 'number1' and 'number2' must be provided.")

        result = float(number1) + float(number2)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'result': result
            })
        }
    except ValueError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'error': str(e)
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': "An error occurred.",
                'details': str(e)
            })
        }
