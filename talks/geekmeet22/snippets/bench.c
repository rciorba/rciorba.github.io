static void
benchmark_getitem(HashIndex *index, char *keys, int key_count)
{
  char *key = keys;
  char *last_addr = key + (32 * key_count);
  while (key < last_addr) {
    hashindex_get(index, key);
    key += 32;
  }
}
