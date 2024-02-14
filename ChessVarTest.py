# Author: Dominic Fantauzzo
# GitHub username: fantauzd
# Date: 11/26/2023
# Description: Tests for ChessVar

from ChessVar import *
import unittest


class TestChessVar(unittest.TestCase):

    def test_full_game(self):
        """
        Play a full game of variant chess and make sure game state and moves are working correctly.
        Game is won by Black capturing both white Knights.
        """
        game = ChessVar()
        self.assertTrue(game.make_move('a2', 'a4'))
        self.assertTrue(game.make_move('b7', 'b6'))
        self.assertTrue(game.make_move('a4', 'a5'))
        self.assertTrue(game.make_move('b6', 'a5'))
        self.assertTrue(game.make_move('b1', 'c3'))
        self.assertTrue(game.make_move('a5', 'a4'))
        self.assertTrue(game.make_move('c3', 'a4'))
        self.assertTrue(game.make_move('b8', 'c6'))
        self.assertTrue(game.make_move('g1', 'f3'))
        self.assertTrue(game.make_move('d7', 'd5'))
        self.assertTrue(game.make_move('e2', 'e3'))
        self.assertTrue(game.make_move('c6', 'e5'))
        self.assertTrue(game.make_move('f3', 'e5'))  # Black Knight Taken
        self.assertEqual(game.get_game_state(), 'UNFINISHED')
        self.assertTrue(game.make_move('e8', 'a4'))  # White Knight Taken
        self.assertEqual(game.get_game_state(), 'UNFINISHED')
        self.assertTrue(game.make_move('e5', 'c4'))
        self.assertTrue(game.make_move('a4', 'c4'))
        self.assertEqual(game.get_game_state(), 'BLACK_WON')
        self.assertFalse(game.make_move('b2', 'b3'))

    def test_full_game_2(self):
        """
        Play a full game of variant chess and make sure game state and moves are working correctly.
        Game is won by White capturing the Black Queen.
        """
        game = ChessVar()
        self.assertTrue(game.make_move('d2', 'd4'))
        self.assertTrue(game.make_move('e7', 'e5'))
        self.assertTrue(game.make_move('c1', 'g5'))
        self.assertTrue(game.make_move('f8', 'e7'))
        self.assertTrue(game.make_move('d4', 'e5'))
        self.assertTrue(game.make_move('e7', 'g5'))
        self.assertTrue(game.make_move('g1', 'f3'))
        self.assertTrue(game.make_move('f7', 'f6'))
        self.assertTrue(game.make_move('e5', 'f6'))
        self.assertTrue(game.make_move('g5', 'f6'))
        self.assertTrue(game.make_move('a2', 'a4'))
        self.assertTrue(game.make_move('e8', 'e4'))
        self.assertTrue(game.make_move('a1', 'a3'))
        self.assertTrue(game.make_move('a7', 'a5'))
        self.assertTrue(game.make_move('a3', 'e3'))
        self.assertTrue(game.make_move('e4', 'a4'))
        self.assertTrue(game.make_move('e3', 'e4'))
        self.assertTrue(game.make_move('a4', 'e4'))
        self.assertTrue(game.make_move('b1', 'c3'))
        self.assertTrue(game.make_move('e4', 'c6'))
        self.assertTrue(game.make_move('b2', 'b3'))
        self.assertTrue(game.make_move('c6', 'c3'))
        self.assertTrue(game.make_move('f3', 'g1'))
        self.assertTrue(game.make_move('c3', 'c2'))
        self.assertTrue(game.make_move('d1', 'c2'))
        self.assertEqual(game.get_game_state(), 'WHITE_WON')

    def test_pawn(self):
        """
        tests all move directions for pawn, including attacks toward both color pieces and empty spaces
        """
        game = ChessVar()
        self.assertTrue(game.make_move('a2', 'a4'))
        self.assertTrue(game.make_move('c7', 'c5'))
        self.assertTrue(game.make_move('b2', 'b3'))
        self.assertTrue(game.make_move('b7', 'b6'))
        self.assertTrue(game.make_move('e2', 'e4'))
        self.assertTrue(game.make_move('e7', 'e5'))
        self.assertFalse(game.make_move('e4', 'd5'))
        self.assertFalse(game.make_move('e4', 'e5'))
        self.assertFalse(game.make_move('e4', 'f5'))
        self.assertFalse(game.make_move('e4', 'f4'))
        self.assertFalse(game.make_move('e4', 'f3'))
        self.assertFalse(game.make_move('e4', 'e3'))
        self.assertFalse(game.make_move('e4', 'd3'))
        self.assertFalse(game.make_move('e4', 'd4'))
        self.assertFalse(game.make_move('e4', 'e6'))
        self.assertTrue(game.make_move('d2', 'd4'))
        self.assertTrue(game.make_move('e5', 'd4'))
        self.assertTrue(game.make_move('e4', 'e5'))
        self.assertTrue(game.make_move('d7', 'd6'))
        self.assertFalse(game.make_move('e5', 'd4'))
        self.assertTrue(game.make_move('e5', 'd6'))
        self.assertFalse(game.make_move('a7', 'b6'))

    def test_castle(self):
        """
        tests all move directions and scenarios for castle.
        """
        game = ChessVar()
        self.assertTrue(game.make_move('a2', 'a4'))
        self.assertTrue(game.make_move('h7', 'h5'))
        self.assertTrue(game.make_move('a1', 'a3'))
        self.assertFalse(game.make_move('h8', 'h4'))
        self.assertFalse(game.make_move('h8', 'h9'))
        self.assertFalse(game.make_move('h8', 'i8'))
        self.assertFalse(game.make_move('h8', 'g8'))
        self.assertTrue(game.make_move('h8', 'h6'))
        self.assertTrue(game.make_move('a3', 'e3'))
        self.assertTrue(game.make_move('h6', 'e6'))
        self.assertFalse(game.make_move('e3', 'e2'))
        self.assertFalse(game.make_move('e3', 'e7'))
        self.assertTrue(game.make_move('e3', 'e6'))
        self.assertTrue(game.make_move('a7', 'a5'))
        self.assertTrue(game.make_move('e6', 'h6'))
        self.assertFalse(game.make_move('a8', 'a5'))
        self.assertFalse(game.make_move('a8', 'a9'))
        self.assertFalse(game.make_move('a8', 'z8'))
        self.assertTrue(game.make_move('a8', 'a6'))
        self.assertTrue(game.make_move('h6', 'a6'))
        self.assertEqual(game.get_game_state(), 'WHITE_WON')

    def test_knight(self):
        """
        tests all move directions and scenarios for knight.
        """
        game = ChessVar()
        self.assertFalse(game.make_move('b8', 'c6'))
        self.assertFalse(game.make_move('b1', 'd2'))
        self.assertFalse(game.make_move('b1', 'd0'))
        self.assertTrue(game.make_move('b1', 'a3'))
        self.assertTrue(game.make_move('g8', 'f6'))
        self.assertTrue(game.make_move('a3', 'c4'))
        self.assertTrue(game.make_move('b8', 'c6'))
        self.assertFalse(game.make_move('c4', 'b2'))
        self.assertFalse(game.make_move('c4', 'd2'))
        self.assertFalse(game.make_move('c4', 'e7'))
        self.assertFalse(game.make_move('c4', 'f3'))
        self.assertTrue(game.make_move('g1', 'f3'))
        self.assertTrue(game.make_move('c6', 'e5'))
        self.assertTrue(game.make_move('f3', 'e5'))
        self.assertTrue(game.make_move('f6', 'g4'))
        self.assertTrue(game.make_move('e5', 'g4'))
        self.assertEqual(game.get_game_state(), 'WHITE_WON')

    def test_bishop(self):
        """
        Tests all move directions and scenarios for bishop.
        """
        game = ChessVar()
        self.assertTrue(game.make_move('d2', 'd4'))
        self.assertTrue(game.make_move('d7', 'd5'))
        self.assertTrue(game.make_move('e2', 'e4'))
        self.assertTrue(game.make_move('e7', 'e5'))
        self.assertTrue(game.make_move('c1', 'g5'))
        self.assertTrue(game.make_move('f8', 'e7'))
        self.assertFalse(game.make_move('f1', 'b7'))
        self.assertFalse(game.make_move('g5', 'i3'))
        self.assertFalse(game.make_move('g5', 'g3'))
        self.assertTrue(game.make_move('f1', 'd3'))
        self.assertFalse(game.make_move('e7', 'h4'))
        self.assertTrue(game.make_move('e7', 'g5'))
        self.assertFalse(game.make_move('d3', 'c2'))
        self.assertFalse(game.make_move('d3', 'f5'))
        self.assertFalse(game.make_move('d3', 'e4'))
        self.assertTrue(game.make_move('e4', 'd5'))
        self.assertTrue(game.make_move('g5', 'c1'))
        self.assertTrue(game.make_move('d3', 'f5'))
        self.assertTrue(game.make_move('c8', 'f5'))
        self.assertEqual(game.get_game_state(), 'BLACK_WON')

    def test_queen(self):
        """
        Tests all move directions and scenarios for Queen.
        """
        game = ChessVar()
        self.assertTrue(game.make_move('d2', 'd4'))
        self.assertTrue(game.make_move('e7', 'e5'))
        self.assertTrue(game.make_move('d4', 'e5'))
        self.assertTrue(game.make_move('e8', 'e5'))
        self.assertFalse(game.make_move('d1', 'd8'))
        self.assertFalse(game.make_move('d1', 'c1'))
        self.assertFalse(game.make_move('d1', 'c2'))
        self.assertFalse(game.make_move('d1', 'e1'))
        self.assertFalse(game.make_move('d1', 'e2'))
        self.assertFalse(game.make_move('e5', 'e6'))
        self.assertTrue(game.make_move('d1', 'd7'))
        self.assertTrue(game.make_move('e5', 'h2'))
        self.assertTrue(game.make_move('d7', 'c8'))
        self.assertFalse(game.make_move('h2', 'a2'))
        self.assertFalse(game.make_move('h2', 'f2'))
        self.assertFalse(game.make_move('h2', 'i2'))
        self.assertFalse(game.make_move('h2', 'f6'))
        self.assertFalse(game.make_move('h2', 'b5'))
        self.assertFalse(game.make_move('h2', 'h7'))
        self.assertTrue(game.make_move('h2', 'h1'))
        self.assertTrue(game.make_move('c8', 'b7'))
        self.assertTrue(game.make_move('h1', 'h6'))
        self.assertFalse(game.make_move('b7', 'h1'))
        self.assertTrue(game.make_move('b7', 'f3'))
        self.assertTrue(game.make_move('h6', 'c6'))
        self.assertTrue(game.make_move('f3', 'h5'))
        self.assertTrue(game.make_move('c6', 'c3'))
        self.assertTrue(game.make_move('h5', 'a5'))
        self.assertTrue(game.make_move('c3', 'd3'))
        self.assertTrue(game.make_move('a5', 'a6'))
        self.assertTrue(game.make_move('d3', 'a6'))
        self.assertEqual(game.get_game_state(), 'BLACK_WON')

    def test_king(self):
        """
        Tests all move directions and scenarios for king piece.
        """
        game = ChessVar()
        self.assertTrue(game.make_move('e2', 'e4'))
        self.assertTrue(game.make_move('d7', 'd5'))
        self.assertTrue(game.make_move('e1', 'e2'))
        self.assertTrue(game.make_move('d8', 'd7'))
        self.assertTrue(game.make_move('e2', 'd3'))
        self.assertTrue(game.make_move('d7', 'd6'))
        self.assertFalse(game.make_move('d3', 'c2'))
        self.assertFalse(game.make_move('d3', 'd3'))
        self.assertFalse(game.make_move('d3', 'd2'))
        self.assertFalse(game.make_move('d3', 'e4'))
        self.assertTrue(game.make_move('d3', 'd4'))
        self.assertFalse(game.make_move('d6', 'c7'))
        self.assertFalse(game.make_move('d6', 'e7'))
        self.assertFalse(game.make_move('d6', 'd5'))
        self.assertFalse(game.make_move('d6', 'a6'))
        self.assertFalse(game.make_move('d6', 'g6'))
        self.assertFalse(game.make_move('d6', 'f4'))
        self.assertFalse(game.make_move('d6', 'b4'))
        self.assertTrue(game.make_move('d6', 'e5'))
        self.assertTrue(game.make_move('d4', 'd5'))
        self.assertTrue(game.make_move('e5', 'e4'))
        self.assertTrue(game.make_move('d5', 'e4'))
        self.assertEqual(game.get_game_state(), 'WHITE_WON')
