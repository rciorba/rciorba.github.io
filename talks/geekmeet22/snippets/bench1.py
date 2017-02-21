def test_chunk_indexer_getitem(benchmark):
    max_key = 2**20
    index = ChunkIndex(max_key)
    keys = [sha256(H(k)).digest() for k in range(max_key)]
    for key in keys:
        index[key] = (0, 0, 0)

    def do_gets(keys=keys):
        for key in keys:
            index[key]  # noqa

    benchmark.pedantic(do_gets, rounds=200)
