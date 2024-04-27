#3003 킹,퀸,룩,비숍,나이트,폰

King, Queen, Rook, Bishop, Knight, Pawn = map(int, input().split())

li = [1 - King, 1 - Queen, 2 - Rook, 2 - Bishop, 2 - Knight, 8 - Pawn]

print(' '.join(map(str, li)))