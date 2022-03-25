def nums_pre(nums):
    """
    购买数字预处理，如果是个位数，加上0
    :param nums:
    :return:
    """
    if nums:
        if isinstance(nums, list) or isinstance(nums, tuple):
            return ['0{}'.format(int(item)) if int(item) < 10 else str(int(item)) for item in nums]
        else:
            return '0{}'.format(int(nums)) if int(nums) < 10 else str(int(nums))
    else:
        return ''