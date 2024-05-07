'''
Classes Used
  In this implementation, we will abuse Python
  ability to overload operators (e.g., ==, !=, <=, etc).

  This makes writing algorithms easier but may
  lead to unintended behavior when not careful.
  
  In particular, as most of these deal with set,
  total order may not be achieved (i.e., not (X < Y) != (X >= Y))
'''
# Set of Attributes
class Attrs():
  def __init__(self, *attrs):
    self._comp = frozenset(attrs)
    self.attrs = tuple(map(lambda attr: attr.upper(), self._comp))
    self._sort = tuple(sorted(self.attrs))

  def copy(self):
    return Attrs(*self.attrs)

  # Abusing Python
  # 1. Relational
  def __hash__(self):
    return hash(self._sort)
  def __repr__(self):
    return ''.join(self._sort)

  def __eq__(this, that):
    return type(this) == type(that) and this._comp == that._comp
  def __ne__(this, that):
    return not (this == that)
  def __le__(this, that):
    return type(this) == type(that) and this._comp <= that._comp
  def __lt__(this, that):
    return type(this) == type(that) and this._comp <  that._comp
  def __ge__(this, that):
    return type(this) == type(that) and this._comp >= that._comp
  def __gt__(this, that):
    return type(this) == type(that) and this._comp >  that._comp

  # 2. Operations
  def __or__ (this, that):
    return Attrs(*(this._comp | that._comp))
  def __and__(this, that):
    return Attrs(*(this._comp & that._comp))
  def __sub__(this, that):
    return Attrs(*(this._comp - that._comp))

  # This is a powerset operation
  #   do not worry about the details
  def __pos__(self):
    res = []
    for i in range(1, 1 << len(self.attrs)):
      res.append(Attrs(*[self.attrs[bit] for bit in range(len(self.attrs)) if (i & (1 << bit)) > 0]))
    return res

  # 3. Loops
  def __iter__(self):
    return self.attrs.__iter__();

# Relations
class Rel():
  def __init__(self, name, attrs):
    self.name  = name
    self.attrs = attrs
  
  # Abusing Python
  # 1. Relational
  def __hash__(self):
    return hash(self.attrs)
  def __repr__(self):
    return f'{self.name}({self.attrs})'

  def __eq__(this, that):
    return type(this) == type(that) and this.attrs == that.attrs
  def __ne__(this, that):
    return not (this == that)
  def __le__(this, that):
    return type(this) == type(that) and this.attrs <= that.attrs
  def __lt__(this, that):
    return type(this) == type(that) and this.attrs <  that.attrs
  def __ge__(this, that):
    return type(this) == type(that) and this.attrs >= that.attrs
  def __gt__(this, that):
    return type(this) == type(that) and this.attrs >  that.attrs

  # 2. Operations
  def __or__ (this, that):
    return Rel(this.name, (this.attrs | that.attrs))
  def __and__(this, that):
    return Rel(this.name, (this.attrs & that.attrs))
  def __sub__(this, that):
    return Rel(this.name, (this.attrs - that.attrs))

  # This is a powerset operation
  #   do not worry about the details
  def __pos__(self):
    return self.attrs.__pos__()

  # 3. Loops
  def __iter__(self):
    return self.attrs.__iter__();

# Functional Dependencies
class FD():
  def __init__(self, src, dst): # (src:Attrs) -> (dst:Attrs)
    self.src = src
    self.dst = dst
    self._ky = (src, dst)
  
  # Abusing Python
  # 1. Relational
  def __hash__(self):
    return hash(self._ky)
  def __repr__(self):
    return f'{{{self.src}}} -> {{{self.dst}}}'

  def __eq__(this, that):
    return type(this) == type(that) and this._ky == that._ky
  def __ne__(this, that):
    return not (this == that)
  def __le__(this, that):
    return type(this) == type(that) and this._ky <= that._ky
  def __lt__(this, that):
    return type(this) == type(that) and this._ky <  that._ky
  def __ge__(this, that):
    return type(this) == type(that) and this._ky >= that._ky
  def __gt__(this, that):
    return type(this) == type(that) and this._ky >  that._ky

# Set of Functional Dependencies
class Sigma():
  def __init__(self, *fds):
    self._ky = set(fds)
    self.fds = tuple(sorted(self._ky))
  
  # Abusing Python
  # 1. Relational
  def __hash__(self):
    return hash(self.attrs)
  def __repr__(self):
    return f'{{{", ".join(list(map(lambda fd: fd.__repr__(), self.fds)))}}}'

  def __eq__(this, that):
    return type(this) == type(that) and this._ky == that._ky
  def __ne__(this, that):
    return not (this == that)
  def __le__(this, that):
    return type(this) == type(that) and this._ky <= that._ky
  def __lt__(this, that):
    return type(this) == type(that) and this._ky <  that._ky
  def __ge__(this, that):
    return type(this) == type(that) and this._ky >= that._ky
  def __gt__(this, that):
    return type(this) == type(that) and this._ky >  that._ky

  # 2. Operations
  def __or__ (this, that):
    return Sigma(*(this._ky | that._ky))
  def __and__(this, that):
    return Sigma(*(this._ky & that._ky))
  def __sub__(this, that):
    return Sigma(*(this._ky - that._ky))

  # 3. Loops
  def __iter__(self):
    return self.fds.__iter__();
