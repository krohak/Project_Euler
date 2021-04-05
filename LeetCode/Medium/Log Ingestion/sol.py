from copy import deepcopy     
import fileinput
import json


class User(object):
    def __init__(self, id, opted_in):
        self.id = id
        self.opted_in = opted_in


class OptInChange(object):
    def __init__(self, user_id, action):
        self.user_id = user_id
        self.action = action


def find_users_with_opt_change(current_user_list, opt_in_change_log):
    
    old_user_dict = { user.id: user.opted_in for user in current_user_list }
    new_user_dict = deepcopy(old_user_dict)
    
    for change in opt_in_change_log:
        if change.user_id not in old_user_dict:
            old_user_dict[change.user_id] = False
        
        action = True if change.action=='opt_in' else False
        new_user_dict[change.user_id] = action
            
    old_user_set = set(old_user_dict.items())
    new_user_set = set(new_user_dict.items())
    
    diff = old_user_set.union(new_user_set) - old_user_set.intersection(new_user_set)
    diff_ids = sorted(set( [ change[0] for change in diff ] ))
    return diff_ids
    

if __name__ == "__main__":
    input_dict = json.loads(''.join([
        line.strip()
        for line in list(fileinput.input())
    ]))

    users = []
    opt_in_change_log = []

    
    for user in input_dict['users']:
        users.append(User(user['id'], user['opted_in']))

    for change_log_line in input_dict['change_log']:
        opt_in_change_log.append(OptInChange(
            change_log_line['user_id'],
            change_log_line['action'],
        ))

    print(','.join(
        str(user) for user in find_users_with_opt_change(users, opt_in_change_log)
    ))



"""
    Sample Input:
        current_user_list: [
            User({
                id: 1,
                opted_in: false
            }),
            User({
                id: 19,
                opted_in: true
            }),
            User({
                id: 4,
                opted_in: true
            }),
            User({
                id: 54,
                opted_in: false
            })
        ]

        opt_in_change_log: [
            OptInChange({
                user_id: 19,
                action: 'opt_out'
            }),
            OptInChange({
                user_id: 1,
                action: 'opt_in'
            }),
            OptInChange({
                user_id: 71,
                action: 'opt_in'
            }),
            OptInChange({
                user_id: 19,
                action: 'opt_in'
            })
        ]

    Sample Output:
        [ 1, 71 ]

        {
  "users": [
    {
      "opted_in": false,
      "id": 2
    },
    {
      "opted_in": true,
      "id": 1
    },
    {
      "opted_in": true,
      "id": 5
    },
    {
      "opted_in": false,
      "id": 3
    },
    {
      "opted_in": false,
      "id": 4
    },
    {
      "opted_in": true,
      "id": 6
    },
    {
      "opted_in": true,
      "id": 8
    },
    {
      "opted_in": false,
      "id": 10
    },
    {
      "opted_in": false,
      "id": 14
    },
    {
      "opted_in": true,
      "id": 19
    },
    {
      "opted_in": true,
      "id": 91
    },
    {
      "opted_in": false,
      "id": 111
    }
  ],
  "change_log": [
    {
      "action": "opt_out",
      "user_id": 19
    },
    {
      "action": "opt_in",
      "user_id": 1
    },
    {
      "action": "opt_in",
      "user_id": 21
    },
    {
      "action": "opt_in",
      "user_id": 71
    },
    {
      "action": "opt_in",
      "user_id": 19
    },
    {
      "action": "opt_out",
      "user_id": 71
    },
    {
      "action": "opt_in",
      "user_id": 14
    },
    {
      "action": "opt_out",
      "user_id": 19
    },
    {
      "action": "opt_in",
      "user_id": 111
    },
    {
      "action": "opt_in",
      "user_id": 22
    },
    {
      "action": "opt_out",
      "user_id": 21
    }
  ]
}
"""