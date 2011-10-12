Vagrant::Config.run do |config|
  config.vm.box = "lapsite"
  config.vm.box_url = "http://files.vagrantup.com/lucid32.box"
  config.vm.network "33.33.33.12"

  config.vm.provision :chef_solo do |chef|
    chef.cookbooks_path = ["cookbooks/opscode",
                           "cookbooks/slab",
                           "cookbooks/err"]

    chef.add_recipe "lap"
    chef.add_recipe 'tmux'
    chef.add_recipe 'vim'

    chef.json = {
      :mysql_password => "w_lap",
      :vim => {
        :extra_packages => %w{vim-scripts exuberant-ctags ack-grep htop}
      },
      :domain => [],
      :openldap => {}
    }
  end
end
