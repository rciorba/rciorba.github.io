Elixir first impressions
========================

As I'll be exploring Elixir, I'm going to write down my thoughts and impressions, mostly
because it's a good way to cement what I'm learning.

Where am I coming from? I have some Erlang knowledge and, as I'm diving in to Elixir, I
find myself looking for the similarities (there are obviously many) and the differences.
Also, for a full disclaimer, I have to warn you that all of my assumptions are probably
shaped (sometimes maybe without me realizing it) by over 10 years of Python.

# Notable differences and new concepts

## The ones I really like

### Structs

Basically just Maps, but with a declared structure. Unlike regular maps that would allow
one to add any key, structs enforce the schema. Those familiar with how Erlang records are
built on top of tuples, will see a similarity in how Structs are built on top of Maps.

I've felt the need for something like this in Erlang when I had used a map as config for
an application. I had a bunch of very hard to debug test failures because I had
missconfigured the app, but I hadn't checked upfront if everything in the config was ok. I
ended up writing some check code myself and, reading about structs, I think they would
have been a perfect fit for my problem.

### Strings
Erlang was notorious for it's poor handling of strings. Thankfully Erlang has gotten
better at this, and now using binaries as strings is the preffered approach. Elixir
embraces the binary string and makes the syntax less cumbersome.

Binary strings no longer need 3 characters to open, and another 3 to close.
```
iex(1)> "a"
"a"
iex(2)> <<"a">>
"a"
```

Because compatibillity with Erlang is important, the classic Erlang string (which is a
list of integers) is also available. In Elixir it's called a charlist.

Charlists, classic Erlang strings:
```
iex(3)> 'A'
'A'
iex(4)> [65]
'A'
```

The only problem I can see is that having both type of strings must be confusing for
people who come to Elixir without knowing the history of Erlang, especially since it's
only a single vs double quote that differetiates them visually.

### Enumerables
Implement this interface... mea culpa, we're supposed call it a protocol...

So implement this protocol and your data type can be used with the Enum module, which
implements common operations like sort, filter, map, reduce, etc.

I can't get in to the details of this, because I've only skimmed the surface, but I like
that there's a way to implement your own collections, that compose well with the rest of
the language.

### Ranges
A Range is a sequence of ascending or descending consecutive integers. Very much like
Python's range, only you can't specify a custom step. They're efficient because ony the
start and end are stored in memory.

### Streams
As the name suggests Streams provide a way to stream data one item at a time. You can
think of them like unix pipes. Sadly Elixir's pipe operator (`|>`) might resemble pipes,
but it's just syntactic sugar for composing function calls. So while they look similar,
unlike pipes data is not passed to the next function as soon as it's available, but it's
passed when the function completes execution.


Let's write a small data transformation pipeline. We want to take a sequence of numbers,
double each number, then sum them.

The following:
```
Enum.map(1..3, &(&1 * 2)) |> Enum.sum()
```

is just syntactic sugar for:
```
Enum.sum(
    Enum.map(1..3, &(&1 * 2))
)
```

Let's have a closer look at `Enum.map`. It builds and returns a new list.
```
iex(4)> Enum.map(1..3, &(&1 * 2))
[2, 4, 6]
```

Looking at the full example, notice how `Enum.sum` is only called at the very end, once
`Enum.map` has built a new list and returned it. Wouldn't it be nice if we didn't have to
build up the whole list, but rather pass along a partial result as soon as we've processed
one element? If you're familiar with Python this is where you'd use a generator (the yield
keyword was one of the things that made me love Python when I first learned it).

This is where Elixir's Streams come in.

We're not in kansas anymore:
```
iex(17)> Stream.map(1..3, &(&1 * 2))
#Stream<[enum: 1..3, funs: [#Function<49.131689479/1 in Stream.map/2>]]>
```

The Stream module provides tools to implement lazy composable data pipelines.
Let's change the doubling and summing pipeline to use Streams:
```
# let's define a function that echos any value passed to it, then returns it
iex(41)> echo = fn(el) -> IO.write("echo:"); IO.puts(el); el; end
#Function<6.128620087/1 in :erl_eval.expr/5>

# now let's re-write our pipeline, and let's toss in our echo function
# in the middle to sneak a peek at values as they pass trough

iex(42)> Stream.map(1..3, &(&1*2)) |> Stream.map(echo) |> Enum.sum()
echo:2
echo:4
echo:6
12
```

Erlang Solutions have a really good article about using Streams for effiency gains:
https://www.erlang-solutions.com/blog/building-an-elixir-stream.html

### Use

Maybe it's because of my Python background, but sometimes I found myself yearning for
something like inheritance to reduce boilerplate in my Erlang code. So I'm very happy to
see Elixir's `use`.

Now while it might look like inheritance at first glance, it's actually macro expansion. I
can't say much more about this because I haven't really used it yet

### Modules in the shell

This might not be a huge deal, but for me it's great I can use the shell to quickly test
out an ideea.

## Those I'm not sure about

### Rebinding variables

In Elixir, unlike in Erlang, you can rebind variables. Unless you've programmed Erlang
before the next snippet of code will probably feel very natural for you. For me it's
uncanny valley.

```
iex(5)> {a, b} = {1, 2}
{1, 2}

iex(6)> {a, b}
{1, 2}

iex(7)> {a, b} = {2, 2}
{2, 2}

iex(8)> a
2
```

Pattern matching is much like in Erlang. For example, this can't match because a would be
bound to two distinct values:

```
{a, a} = {1, 2}
** (MatchError) no match of right hand side value: {1, 2}
```

This is OK.
```
{a, a} = {2, 2}
```

To avoid rebinding a variable you must use the pin operator `^`.

This attempts to match a and leaves b to be (re)bound.
```
{^a, b} = {1, 2}
```

Also, just like Erlang, anything on the righ hand side will never be bound, only
matched. So the following will never bind a or b, instead it will attempt a match:

```
{1, 2} = {a, b}
```

The downside for Erlang's match-unless-bound is you need to know which variables are
already bound. Elixir's pin operator is more explicit.

### Lower case variables, atoms and aliases

Erlang's approach, where anything that starts with a lowercase letter is an atom, and
anything capitalized is a variable, is just another one of it's quirks. Maybe you saw some
Elixir code, noticed all those lowercase variables, `:` as a prefix for atoms, and assumed
capitalization doesn't matter in Elixir... nope, capitaization still matters in Elixir. If
you type a capitalized word, because of another feature called Aliasing, you get an atom.

Elixir atoms:
```
iex(1)> is_atom(:abc)
true

iex(2)> to_string(:abc)
"abc"

iex(3)> is_atom(Abc)
true

iex(4)> Abc
Abc

iex(5)> to_string(Abc)
"Elixir.Abc"
```

I'd file this as a superficial difference however it adds one small problem, variables can
now potentially shadow functions. So when you write `is_number(1)` are you calling
`Kernel.is_number/1` or are you calling an anonymous function bound to the variable
`is_number`? In order to avoid the ambiguity in Elixir you have to add a dot after the
variable name when calling anonymous functions. So if you have a local varibale named
is_number bound to a fun and want to call it, you'd use `is_number.(1)`.

# Some early conclusions
At the end of the day, it's basically still Erlang and, I think it's safe to say, most
people who like Erlang like it despite the syntax.

The biggest change for me would be the larger surface area. Erlang is actually a small
language. Elixir adds lots of creature comforts, but that means more stuff to learn.

Conditionals? In addition to Erlang's `cond` and `if` we also have `unless`.

Aliases. A whole new concept.

Nested modules? I need to learn more about these, but they seem to be just plain old
modules, with a dot in the name :).


