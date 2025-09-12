import json
import os


# Base do projeto
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "mock_aws"))
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
LOGS_DIR = os.path.join(BASE_DIR, "logs")
S3_DIR = os.path.join(BASE_DIR, "s3")


def lambda_handler(event, context=None):
	# Decodifica body se vier de Lambda1
	if isinstance(event, dict) and "body" in event:
		try:
			event = json.loads(event["body"])
		except Exception:
			pass

	# Cria pastas se não existirem
	os.makedirs(OUTPUT_DIR, exist_ok=True)
	os.makedirs(LOGS_DIR, exist_ok=True)
	os.makedirs(S3_DIR, exist_ok=True)

	# Salva resultado em outputs
	file_name = "resultado.json"
	file_path = os.path.join(OUTPUT_DIR, file_name)
	with open(file_path, "w", encoding="utf-8") as f:
		f.write(json.dumps(event, indent=2, ensure_ascii=False))

	# Cria log fictício
	log_file = os.path.join(LOGS_DIR, "exemplo-log.txt")
	with open(log_file, "w", encoding="utf-8") as f:
		f.write("[2025-09-10 10:00:00] Workflow simulado: Lambda2 processou dados.\n")

	# Cria arquivo de exemplo simulando S3
	s3_file = os.path.join(S3_DIR, "exemplo-arquivo.txt")
	with open(s3_file, "w", encoding="utf-8") as f:
		f.write("Arquivo exemplo simulando bucket S3\n")

	return {
		"status": "Arquivo salvo (mock do S3)",
		"path": file_path
	}


if __name__ == "__main__":
	evento_teste = {"id": 1, "mensagem": "Teste local Lambda2"}
	resultado = lambda_handler(evento_teste)
	print("Lambda2 mock resultado:", resultado)
