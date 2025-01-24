#импорт
import utaupy

#функции для понижения 
def semitones_down(ust, semitones):
    for note in ust.notes:
        note.notenum -= semitones

# открытие уста
input_path = 'PyrokinesisM.ust'
ust = utaupy.ust.load(input_path)

# понижает на 5 полутонов
semitones_down(ust, 5)

# сохраняет уст
output_path = 'Harm.ust'
ust.write(output_path, encoding='shift_jis')

print(f"Файл сохранен: {output_path}")