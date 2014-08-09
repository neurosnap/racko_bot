Rack-o Bot
==========

Rack-o game bot

.. code::python

	import racko
	game = racko.game.Dealer(60, [racko.bot.Player("Sue"), racko.bot.Player("Roxanne")])

	game.deal()
	game.next_turn()