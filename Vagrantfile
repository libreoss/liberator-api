# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

VAGRANT_LOCAL_CONFIG = "vagrant-conf.local"

load(VAGRANT_LOCAL_CONFIG) if File.exist?(VAGRANT_LOCAL_CONFIG) # include local configuration if available

VAGRANT_ARCH = "x64" unless defined? VAGRANT_ARCH

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.define "liberator" do |liberator|
        liberator.vm.box = "debian"
        if VAGRANT_ARCH == "x64"
            liberator.vm.box_url = "https://ftp.lugons.org/vagrant/debian-7.6.0-x86_64.box"
        else
            liberator.vm.box_url = "https://dl.dropboxusercontent.com/s/60pv9an852jx9y0/Debian-7.3.0-i386b.box?dl=1"
        end

        liberator.vm.network :private_network, ip: "192.168.66.6"
        config.vm.boot_timeout = 600
        liberator.vm.provision :ansible do |ansible|
            ansible.playbook = "provision/site.yml"
            ansible.host_key_checking = false
            ansible.groups = {
                "vagrant" => ["liberator"],
            }
        end
    end
end
