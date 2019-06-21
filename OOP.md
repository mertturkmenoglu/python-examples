# OOP Concept Comparison
***
1. Constructors:
    * **Java**:
    ```java
        public class Person {
            private String name;
            private int age;

            public Person(String name, int age) {
                this.name = name;
                this.age = age;
            }
        }
    ```
    * **Python**:
    ```python
        class Person:
            
            def __init__(self, name, age):
                self.__name = name
                self.__age = age

    ```
2. Static member fields:
    * **Java**:
    ```java
        public class Person {
            public static int n = 0;
            public Person() { }
        }
    ```
    * **Python**:
    ```python
        class Person:
            n = 0
            def __init__(self):
                pass

    ```
3. Inheritance:
    * **Java**:
    ```java
        public class Person extends Human {
            public Person(String name, int age) {
                super(name, age);
            }
        }
    ```
    * **Python**:
    ```python
        class Person(Human):
            def __init__(self, name, age):
                super.__init__(name, age)

    ```
4. Encapsulation:
    * **Java**:
    ```java
        public class Person {
            private String name;
            private int age;

            public Person(String name, int age) {
                this.name = name;
                this.age = age;
            }

            public String getName() {
                return name;
            }

            public int getAge() {
                return age;
            }

            public void setName(String name) {
                this.name = name;
            }

            public void setAge(int age) {
                this.age = age;
            }
        }
    ```
    * **Python**:
    ```python
        class Person:
            def __init__(self, name, age):
                self.__name = name
                self.__age = age

            def get_name(self):
                return self.__name

            def get_age(self):
                return self.__age

            def set_name(self, name):
                self.__name = name

            def set_age(self, age):
                self.__age = age

            name = property(get_name, set_name)
            age = property(get_age, set_age)

    ```
5. Operator Overloding:
    * **C++**:
    ```cpp
        class Vector2D
        {
        public:
            double x;
            double y;
        public:
            Vector2D(double x, double y) : x(x), y(y) { }

            Vector2D operator+(const Vector2D& other) const {
                return Vector2D(this->x + other.x, this->y + other.y);
            }
        }
    ```
    * **Python**:
    ```python
        class Vector2D:
            def __init__(self, x, y):
                self.x = x
                self.y = y

            def __add__(self, other):
                return Vector2D(self.x + other.x, self.y + other.y)

    ```