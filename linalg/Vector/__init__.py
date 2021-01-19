import math


class Vector2(tuple):
    """
    Provides (for a, b vectors, k number):
       a+b vector addition
       a-b vector subtraction
       a*b inner product
       k*a and a*k multiplication with scalar
       |a| absolute value of a
       a.rotate(angle) rotation
    """

    def __new__(cls, x, y):
        return tuple.__new__(cls, (x, y))

    # Overload "+" operator
    def __add__(self, other):
        return Vector2(self[0] + other[0], self[1] + other[1])

    # Overload "-" operator
    def __sub__(self, other):
        return Vector2(self[0] - other[0], self[1] - other[1])

    def __mul__(self, other):
        if isinstance(other, Vector2):
            return self[0] * other[0] + self[1] * other[1]
        return Vector2(self[0] * other, self[1] * other)

    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector2(self[0] * other, self[1] * other)

    def __neg__(self):
        return Vector2(-self[0], -self[1])

    def __abs__(self):
        return (self[0] ** 2 + self[1] ** 2) ** 0.5

    def rotate(self, angle):
        """rotate self counterclockwise by angle
        """
        perp = Vector2(-self[1], self[0])
        angle = angle * math.pi / 180.0
        c, s = math.cos(angle), math.sin(angle)
        return Vector2(self[0] * c + perp[0] * s, self[1] * c + perp[1] * s)

    def __getnewargs__(self):
        return (self[0], self[1])

    def __repr__(self):
        return "(%.2f,%.2f)" % self


class Vector3:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # set to zero vector
    def zero(self):
        self.x = 0
        self.y = 0
        self.z = 0

    # "=" does not support overload

    # Overload "==" operator
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    # Overload "!=" operator
    def __ne__(self, other):
        return self.x != other.x or self.y != other.y or self.z != other.z

    # Overload singular "-" operator
    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    # Overload "+" operator
    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    # Overload "-" operator
    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    # Overload "*" operator
    def __mul__(self, a):
        return Vector3(self.x * a, self.y * a, self.z * a)

    # Overload "/" operator
    def __div__(self, a):
        if (a != 0):
            return Vector3(self.x / a, self.y / a, self.z / a)
        else:
            return None

    # Overload "+=" operator
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    # Overload "-=" operator
    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    # Overload "*=" operator
    def __imul__(self, a):
        self.x *= a
        self.y *= a
        self.z *= a
        return self

    # Overload "/=" operator
    def __idiv__(self, a):
        if (a != 0):
            self.x /= a
            self.y /= a
            self.z /= a
        return self

    # normalize vector
    def normalize(self):
        magSq = self.x * self.x + self.y * self.y + self.z * self.z
        if (magSq > 0):
            oneOverMag = 1.0 / math.sqrt(magSq)
            self.x *= oneOverMag
            self.y *= oneOverMag
            self.z *= oneOverMag

    # mode of a vector
    def vectorMag(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    # show vector
    def toString(self):
        print(
            "{x:" + str(self.x) + ",y:" + str(self.y) + ",z:" + str(self.z) + "}"
        )

    # inner product
    def dotProduct(va, vb):
        return va.x * vb.x + va.y * vb.y + va.z * vb.z

    # cross product
    def crossProduct(va, vb):
        x = va.y * vb.z - va.z * vb.y
        y = va.z * vb.x - va.x * vb.z
        z = va.x * vb.y - va.y * vb.x
        return Vector3(x, y, z)

    # calculate distance between two point
    def distance(va, vb):
        dx = va.x - vb.x
        dy = va.y - vb.y
        dz = va.z - vb.z
        return math.sqrt(dx * dx + dy * dy + dz * dz)
