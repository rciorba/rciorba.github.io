### So I tried to compile juju-core..

I started off like every impaciend developer does,
clone the source and look for a Readme, and a Makefile.

Only to discover that in the somwhat long while since I've last used golang
it seems to have grown a `go get` command that should sort out all fetching
and building of dependencies. This all sounds great, but in practice it's not
entirely smooth sailing. It looks like the dependency manager has no notion
of pinned dependencies, it just fetches the latest revisions and hopes for the best.

At least the build mechanism is simple enought that you can just checkout
different revisions and rebuild (code is in $GOPATH/src/)

The problem packages:
 1. code.google.com/p/go.crypto I had to revert it to 191 (2990fc550b9f), just
    before they imported gosshnew
 2. github.com/juju/ratelimit This one is a case of a trivial refactor,
    renaming a few functions, so I updated worker/instancepoller/aggregate.go accordingly
    https://github.com/juju/ratelimit/commit/5d76fccf915154e3c8f8fadebd4eafdf4ff9b0b9
