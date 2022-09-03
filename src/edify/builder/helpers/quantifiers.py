quantifier_table = {
    'one_or_more': '+',
    'one_or_more_lazy': '+?',
    'zero_or_more': '*',
    'zero_or_more_lazy': '*?',
    'optional': '?',
    'exactly': lambda times: '{{{}}}'.format(times),
    'at_least': lambda times: '{{{},}}'.format(times),
    'between': lambda times: '{{{},{}}}'.format(times[0], times[1]),
    'between_lazy': lambda times: '{{{},{}}}?'.format(times[0], times[1]),
}
