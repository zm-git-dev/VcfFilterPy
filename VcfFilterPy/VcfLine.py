from create_vcf_dict import vcfline2dict
from create_custom_fields import custom_fields
from filter_dict_fields import filter_dict_keys
from test_vcf_line import test_vcf_line

class VcfLine(object):

    def __init__(self, line, csq_keys=None):
        self.line = line
        self.dicts = vcfline2dict(line, csq_keys)
    
    def filter_line(self, conditions, how='any'):
        ''' Test a VcfLine against a set of conditions and return the orginal
            vcf line string if they are met.
        '''
        update_dicts = custom_fields(self.dicts, conditions)
        filtered_dicts = [filter_dict_keys(conditions, x) for x in update_dicts]
        tested_samples = [test_vcf_line(conditions, x) for x in filtered_dicts]

        if how == 'any' and any(tested_samples):
            return self.line

        if how == 'all' and all(tested_samples):
            return self.line
 
    

