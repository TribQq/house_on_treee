install:
	poetry install
test:
	#poetry shell
	# python -m pip freeze > req1.txt
	#pytest .
	#python -m pytest
	poetry run pytest .


#validate:
	#mypy . # hard validation, not need now( typing.List != list LOL)

# мы не можем использовать названия папок, т.к изначально make был создан для билдинга и компиляции => воспринимает директории с {name} как уже выполненную комануд
# позволяет игнорить требоание выше
.PHONY: house_on_treee
house_on_treee:
	poetry run pytest .
