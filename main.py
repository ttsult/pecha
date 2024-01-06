from word_db.db_connection import interact_with_db


running = True
q = ['q','quit','exit']

while running:
    inp = input('What word would you like to be translated?: ')
    translated = interact_with_db().search_db(inp)
    print("HERE is your word: ", translated[1])
    break
    




