
class FeedRecordType:
  RECONNAISSANCE = 1
  WEAPONIZATION = 2
  DELIVERY = 3
  EXPLOIT = 4
  INSTALLATION = 5
  COMMAND_AND_CONTROL = 6
  ACTIONS_ON_OBJECTIVES = 7
  SPAMMING = 8

  _MAPPING = {
      RECONNAISSANCE: 'reconnaissance',
      WEAPONIZATION: 'weaponization',
      DELIVERY: 'delivery',
      EXPLOIT: 'exploit',
      INSTALLATION: 'installation',
      COMMAND_AND_CONTROL: 'command_and_control',
      ACTIONS_ON_OBJECTIVES: 'actions_on_objectives',
      SPAMMING: 'spamming'
      }

  @classmethod
  def to_string(cls, value):
    return cls._MAPPING[value]


