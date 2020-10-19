##
## EPITECH PROJECT, 2019
## makefile
## File description:
## makefile
##

MAIN	=	pong.py

EXEC	=	101pong

all:	$(MAIN)

$(MAIN): python3 $(MAIN)

.PHONIE: clean fclean re

clean:
	rm -f *~
	rm -f '#*#'

fclean:	clean

re:	fclean all
