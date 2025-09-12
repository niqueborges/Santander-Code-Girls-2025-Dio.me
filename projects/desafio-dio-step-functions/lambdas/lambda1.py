import json
import datetime


def lambda_handler(event=None, context=None):
	# Access event and context to avoid unused variable warnings
	_ = event
	_ = context
	data = {
		"id": 1,
		"mensagem": "Processamento concluído com sucesso",
		"timestamp": datetime.datetime.now().isoformat()
	}
	return {
		"statusCode": 200,
		"body": json.dumps(data, ensure_ascii=False)
	}


if __name__ == "__main__":
	resultado = lambda_handler()
	print("Lambda1 mock resultado:", resultado)