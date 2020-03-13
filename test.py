#!/usr/bin/env python3
import sys

myAge = 19
class App:
    def defAge(self, age):
        return age + 10

    def main(self):
        print("my age is: " + str(self.defAge(myAge)))
        sys.exit(0)
        return

if __name__ == "__main__":
    app = App()
    app.main()
