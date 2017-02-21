from cpython.bytes cimport PyBytes_AS_STRING

cdef extern from "_hashindex.c":
    ctypedef struct HashIndex:
        pass

    void benchmark_getitem(HashIndex *index, char *keys, int key_count)

def bench_getitem(ChunkIndex chunk_index, bytes keys):
    cdef int key_count = len(keys) // chunk_index.key_size
    benchmark_getitem(
        chunk_index.index, PyBytes_AS_STRING(keys), key_count)
