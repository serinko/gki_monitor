# TODO
# Calculation of Glucose and Ketose
# User interface
# Time stamp
# Data archive
# Graphs

#  GKI FORMULA IS: GLUCOSE (mg/dL) / 18 / KETONES (mmol/L)


# PROMPTS
msr_prt = ''
gl_prt = ''
kt_prt = ''

# OPTIONS IN CLI:
# 1 Calculate GKI
# 2 Calculate Glucose
# 3 Calculate Ketones
# 4 See past data

# Second level branch
# 1. Is your glusoces in
# 1.1 mg/dL
# 1.2 or in mmol/L
# 2 Is your glusoces in
# 2.1 mg/dL
# 2.2 or in mmol/L
# $ What is the time preference you want to see:
# 4 Do you want to see a graph
# 4.1 Yes - generate tablae and graph
# 4.2 No table is enough - generate graph

msr= input(msr_prt)

if msr == '1':
    gl = float(input(gl_prt))
    kt = float(input(kt_prt))
elif msr == '2':
    gl = float(input(gl_prt))

# GKI CALCULATOR
# What do we measure gl and kt in?
gki_equation = ''
