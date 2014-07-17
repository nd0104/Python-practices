__author__ = 'ND'
sentence = raw_input('Sentence:')
screen_width = 80
text_width = len(sentence)
box_width = text_width+6
left_mergin = (screen_width - box_width)

print
print ' ' * left_mergin + '+' + '-' * text_width  + '+'
print ' ' * left_mergin + '|' + ' ' * text_width  + '|'
print ' ' * left_mergin + '|' +  sentence  + '|'
print ' ' * left_mergin + '|' + ' ' * text_width  + '|'
print ' ' * left_mergin + '+' + '-' * text_width  + '+'