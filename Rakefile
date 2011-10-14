
require 'etc'
require 'fileutils'
require 'vagrant'


task :default => :usage

task :usage do
  puts "You forgot to tell the computer what to do; try one of these commands:"
  system("rake -T")
end

# Execute a command in the primary VM and write its output to the screen.
def vm_ssh(env, cmd)
  puts ">>> '#{cmd}'"
  env.primary_vm.ssh.execute do |ssh|
    ssh.exec!(cmd) do |channel, stream, data|
      print data
      $stdout.flush
    end
  end
end

def createuser(env, username, passwd)
    vm_ssh(env, "sudo su root <<SCRIPT
sudo -u postgres createuser --superuser --createdb --createrole --pwprompt --echo #{username} << EOF
#{passwd}
#{passwd}
EOF
SCRIPT")
end

def createdb(env, username, dbname)
  vm_ssh(env, "sudo su root <<SCRIPT
sudo -u postgres createdb -O #{username} --echo #{dbname}
SCRIPT")
end

desc 'Destroys and initializes the environment.'
task :init => [:clobber,
               :cookbooks,
               'vm:up']

desc 'Cleans everything out of the environment.'
task :clobber do
  FileUtils.rmtree %w{omeka omeka.bk cookbooks}, :verbose => true
  env = Vagrant::Environment.new
  if env.primary_vm.created?
    puts 'vagrant destroy'
    env.cli('destroy')
  end
end

desc 'Downloads the cookbooks.'
task :cookbooks do
  Dir.mkdir("cookbooks") unless File.directory?("cookbooks")
  system('git clone --branch=slab https://github.com/erochest/opscode-cookbooks.git cookbooks/opscode')
  system('git clone https://github.com/scholarslab/cookbooks.git cookbooks/slab')
  system('git clone git://github.com/erochest/cookbooks.git cookbooks/err')
end

namespace :vm do
  desc 'This calls Vagrant up.'
  task :up do
    env = Vagrant::Environment.new
    puts 'vagrant up'
    env.cli('up')
  end

  desc 'Do a safe halt on the VM.'
  task :halt do
    vm_ssh(Vagrant::Environment.new, 'sudo halt')
  end

  desc "cat /tmp/vagrant-chef-1/chef-stacktrace.out."
  task :chefst do
    env = Vagrant::Environment.new
    raise "Must run `vagrant up`" if !env.primary_vm.created?
    raise "Must be running!" if !env.primary_vm.vm.running?
    puts "Getting chef stacktrace."
    vm_ssh(env, "cat /tmp/vagrant-chef-1/chef-stacktrace.out")
  end
end

desc 'Runs the unittests.'
task :test do
  env = Vagrant::Environment.new
  vm_ssh(env, 'PYTHONPATH=/vagrant python -m runpy lapsite.tests')
end

namespace :pg do

  desc 'This configures PostgreSQL for remote logins and users.'
  task :config do
    puts 'Configuring PostgreSQL.'
    env = Vagrant::Environment.new

    vm_ssh(env, %{echo "listen_addresses = '*'" | sudo tee --append /etc/postgresql/8.4/main/postgresql.conf})
    vm_ssh(env, %{echo "local   all         all                               password" | sudo tee --append /etc/postgresql/8.4/main/pg_hba.conf})
    vm_ssh(env, %{echo "hostssl all         all         0.0.0.0/0             password" | sudo tee --append /etc/postgresql/8.4/main/pg_hba.conf})

    Rake::Task['pg:restart'].invoke
  end

  desc 'This restarts PostgreSQL.'
  task :restart do
    puts 'Restarting PostgreSQL.'
    env = Vagrant::Environment.new
    vm_ssh(env, 'sudo /etc/init.d/postgresql-8.4 restart')
  end

  desc 'This creates the vagrant PostgreSQL user.'
  task :createuser do
    puts 'Creating vagrant and w_lap PostgreSQL users.'
    env = Vagrant::Environment.new
    createuser(env, 'vagrant', 'vagrant')
    createuser(env, 'w_lap', 'w_lap')
  end

  desc 'This creates the LAP database.'
  task :createdb do
    puts 'Creating lap database.'
    env = Vagrant::Environment.new
    createdb(env, 'w_lap', 'lap')
  end
end
