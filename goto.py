from ext.goto import goto

@goto
def main():
   
    i = 0

    label .foo
    print(i)

    i += 1

    if i < 10:
      goto .foo

main()
