#! ecoding: utf-8

def get_number(question) :
	while True:
		try:
			user_input = raw_input(question)

			if user_input in ('0', 'exit'):
				break

			user_input = float(user_input)
			return user_input

		except:
			print("Opss, isso não é um numero, retire as letras ou use ponto em lugar de virgula.")

	exit()


if __name__ == '__main__':
	print("\n* Bem vindo a calculadora de IMC (digite 0 ou exit para sair)")

	peso   = get_number("Qual é seu peso? ")
	altura = get_number("Qual é a sua altura? ")
	imc    = peso / (altura * altura)

	print("Seu imc é de %s."%imc)

	if imc < 18.5 :
		print("Seu imc é menor que 18.5, você esta abaixo do peso.")

	elif imc > 18.5 and imc < 24.9 :
			print("Seu imc esta entre 18.5 e 24.9, parabens, você tem um peso ideal. :)")

	elif imc > 24.9 and imc < 29.9 :
		print("Seu imc esta entre 24.9 e 29.9, você esta levemente acima do peso.")

	elif imc > 29.9 and imc < 34.9 :
		print("Seu imc esta entre 29.9 e 34.9, você esta no primeiro grau de obesidade.")

	elif imc > 34.9 and imc < 39.9 :
		print("Seu imc esta entre 34.9 e 39.9, você esta no segundo grau de obesidade. ")

	elif imc > 39.9 :
		print("Seu imc é maior que 39.9, você tem obesidade morbida.")
