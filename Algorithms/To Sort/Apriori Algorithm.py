"""Apriori frequent-itemset mining algorithm."""

from itertools import combinations


def _support(itemset, transactions):
    """Return the fraction of transactions containing ``itemset``."""
    return sum(itemset <= transaction for transaction in transactions) / len(transactions)


def apriori(transactions, min_support=0.5):
    """Find frequent itemsets and their support values.

    Args:
        transactions: An iterable of iterables, where each inner iterable is
            one transaction.
        min_support: Minimum support as a fraction between 0 and 1.

    Returns:
        A dictionary mapping each frequent itemset (a ``frozenset``) to its
        support value.
    """
    if not 0 <= min_support <= 1:
        raise ValueError("min_support must be between 0 and 1")

    transaction_sets = [set(transaction) for transaction in transactions]
    if not transaction_sets:
        return {}

    items = sorted({item for transaction in transaction_sets for item in transaction},
                   key=repr)
    frequent = {}
    candidates = {frozenset((item,)) for item in items}

    while candidates:
        supported = {
            itemset: _support(itemset, transaction_sets)
            for itemset in candidates
            if _support(itemset, transaction_sets) >= min_support
        }
        if not supported:
            break
        frequent.update(supported)

        size = len(next(iter(supported))) + 1
        previous = set(supported)
        candidates = {
            frozenset(items_tuple)
            for items_tuple in combinations(sorted(set().union(*previous), key=repr), size)
            if all(frozenset(subset) in previous
                   for subset in combinations(items_tuple, size - 1))
        }

    return frequent


if __name__ == "__main__":
    transactions = [
        {"bread", "milk"},
        {"bread", "diapers", "beer", "eggs"},
        {"milk", "diapers", "beer", "cola"},
        {"bread", "milk", "diapers", "beer"},
        {"bread", "milk", "diapers", "cola"},
    ]
    for itemset, support in sorted(apriori(transactions, 0.6).items(),
                                   key=lambda pair: (len(pair[0]), sorted(pair[0]))):
        print(f"{set(itemset)}: {support:.2f}")
