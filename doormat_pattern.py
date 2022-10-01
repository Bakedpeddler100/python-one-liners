pattern = [('.|.'*(2*i+1)).center(27, '-') for i in range(5)]
print('\n'.join(pattern+['WELCOME'.center(27, '-')]+pattern[::-1]))
