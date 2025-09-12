from lambda1 import lambda_handler as lambda1_handler
from lambda2 import lambda_handler as lambda2_handler


# Executa Lambda1
resultado_lambda1 = lambda1_handler()


# Passa o resultado para Lambda2
resultado_lambda2 = lambda2_handler(resultado_lambda1)


print("Workflow completo finalizado:", resultado_lambda2)
